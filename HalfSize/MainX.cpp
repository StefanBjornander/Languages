// Stefan Björnander

#include <Map>
#include <Vector>
#include <String>
#include <FStream>
#include <IOStream>
#include <CAssert>
using namespace std;

#include "Header.h"
#include "Pixel.h"
#include "Index.h"
#include "Block.h"
#include "Matrix.h"

enum {NoImageDataIncluded = 0,
      UncompressedColorMappedImage = 1,
      UncompressedColorImage = 2,
      UncompressedGrayScaleImage = 3,
      RunLengthEncodedColorMappedImage = 9,
      RunLengthEncodedColorImage = 10,
      RunLengthEncodedGrayScaleImage = 11};

void loadEmptyImage(Header& header, ifstream& inStream,
                    const string& outName);
void loadUnmappedImage(Header& header, ifstream& inStream,
                       const string& outName, bool compressed);
void loadMappedImage(Header& header, ifstream& inStream,
                     const string& outName, bool compressed);
void generateHalfPixelMatrix(const Matrix<Pixel> &fullPixelMatrix,
                             Matrix<Pixel>& halfPixelMatrix);
void generateHalfIndexMatrix(Header& header,
                             const Matrix<Index> &fullIndexMatrix,
                             Matrix<Index>& halfIndexMatrix,
                             vector<Pixel>& pixelVector,
                             map<Pixel,Index>& pixelToIndexMap);
void optimizeHalfIndexMatrix(Header& header, Matrix<Index>& halfIndexMatrix,
                             vector<Pixel>& pixelVector);
void check(bool test, const string& message);

void main(int argc, char* argv[]) {
  check(argc == 3, "usage: halfsize <inputfile> <outputfile>");
  string inName = argv[1], outName = argv[2];
         
  ifstream inStream(inName, ios::in | ios::binary);
  check((bool) inStream,
        "Error when opening \"" + inName + "\" for reading.");

  cout << "Reading \"" << inName << "\" ..." << endl;
  Header header;
  header.load(inStream);

  check((header.bitsPerPixelOrIndex == 8) ||
        (header.bitsPerPixelOrIndex == 16) ||
        (header.bitsPerPixelOrIndex == 24) ||
        (header.bitsPerPixelOrIndex == 32),
        "Pixels or indices must be 8, 16, 24, or 32 bits.");

  switch (header.dataTypeCode) {
    case NoImageDataIncluded:
      loadEmptyImage(header, inStream, outName);
      break;

    case UncompressedColorImage:
    case UncompressedGrayScaleImage:
      loadUnmappedImage(header, inStream, outName, false);
      break;

    case UncompressedColorMappedImage:
      loadMappedImage(header, inStream, outName, false);
      break;

    case RunLengthEncodedColorImage:
    case RunLengthEncodedGrayScaleImage:
      loadUnmappedImage(header, inStream, outName, true);
      break;

    case RunLengthEncodedColorMappedImage:
      loadMappedImage(header, inStream, outName, true);
      break;

    default:
      check(false, string("Invalid Data Type Code: ") +
                   header.dataTypeCode);
      break;
  }
}

void loadEmptyImage(Header& header, ifstream& inStream,
                    const string& outName) {
  char* idBuffer = new char[header.idLength];
  assert((header.idLength == 0) || (idBuffer != nullptr));
  inStream.read(idBuffer, header.idLength);
  cout << "Done: the image contains no data." << endl;

  ofstream outStream(outName, ios::out | ios::binary);
  check((bool) outStream,
        "Error when opening \"" + outName + "\" for writing.");

  cout << "Saving \"" << outName << "\" ..." << endl;
  header.save(outStream);
  outStream.write(idBuffer, header.idLength);
  cout << "Done.";
}

void loadUnmappedImage(Header& header, ifstream& inStream,
                       const string& outName, bool compressed) {
  check(header.colorMapType == 0,
        "Invalid Color Map Type: " + header.colorMapType);
  char* idBuffer = new char[header.idLength];
  assert((header.idLength == 0) || (idBuffer != nullptr));
  inStream.read(idBuffer, header.idLength);

  Matrix<Pixel> fullPixelMatrix(header.width, header.height, compressed);
  fullPixelMatrix.load(header.bitsPerPixelOrIndex, inStream);
  cout << "Done: the image is unmapped and "
       << (compressed ? "compressed" : "uncompressed") << "." << endl;

  cout << "Original size: " << header.width << "x" << header.height << endl;
  header.width /= 2;
  header.height /= 2;

  Matrix<Pixel> halfPixelMatrix(header.width, header.height, compressed);
  generateHalfPixelMatrix(fullPixelMatrix, halfPixelMatrix);

  ofstream outStream(outName, ios::out | ios::binary);
  check((bool) outStream,
        "Error when opening \"" + outName + "\" for writing.");

  cout << "Saving \"" << outName << "\" ..." << endl;
  header.save(outStream);
  outStream.write(idBuffer, header.idLength);
  halfPixelMatrix.save(outStream);
  cout << "Done.";
}

void generateHalfPixelMatrix(const Matrix<Pixel> &originalPixelMatrix,
                             Matrix<Pixel>& halfPixelMatrix) {
  cout << "Resizing to: " << halfPixelMatrix.width() << "x"
       << halfPixelMatrix.height() << " ..." << endl;

  for (int row = 0; row < halfPixelMatrix.height(); ++row) {
    for (int column = 0; column < halfPixelMatrix.width(); ++column) {
      Pixel pixel1 = originalPixelMatrix.get(2 * row, 2 * column),
            pixel2 = originalPixelMatrix.get(2 * row, (2 * column) + 1),
            pixel3 = originalPixelMatrix.get((2 * row) + 1, 2 * column),
            pixel4 = originalPixelMatrix.get((2 * row) + 1, (2 * column)+1);
      Pixel averagePixel =
        average(pixel1, average(pixel2, average(pixel3, pixel4)));
      halfPixelMatrix.set(row, column, averagePixel);
    }
  }

  cout << "Done." << endl;
}

void loadMappedImage(Header& header, ifstream& inStream,
                     const string& outName, bool compressed) {
  check(header.colorMapType == 1,
        "Invalid Color Map Type: " + header.colorMapType);

  char* idBuffer = new char[header.idLength];
  assert((header.idLength == 0) || (idBuffer != nullptr));
  inStream.read(idBuffer, header.idLength);

  check((header.colorMapDepth == 8) ||
        (header.colorMapDepth == 16) ||
        (header.colorMapDepth == 24) ||
        (header.colorMapDepth == 32),
        "Pixels must be 8, 16, 24, or 32 bits");

  vector<Pixel> pixelVector;
  map<Pixel,Index> pixelToIndexMap;
  for (int count = 0; count < header.colorMapLength; ++count) {
    Pixel pixel;
    pixel.load(header.colorMapDepth, inStream);
    pixelToIndexMap[pixel] =
	  Index(header.bitsPerPixelOrIndex, (int) pixelVector.size());
	pixelVector.push_back(pixel);
  }

  Matrix<Index> fullIndexMatrix(header.width, header.height, compressed);
  fullIndexMatrix.load(header.bitsPerPixelOrIndex, inStream);
  cout << "Done: the image is mapped and "
       << (compressed ? "compressed" : "uncompressed") << "." << endl;

  cout << "Original size: " << header.width << "x" << header.height << endl;
  header.width /= 2;
  header.height /= 2;

  Matrix<Index> halfIndexMatrix(header.width, header.height, compressed);
  generateHalfIndexMatrix(header, fullIndexMatrix, halfIndexMatrix,
                          pixelVector, pixelToIndexMap);
  optimizeHalfIndexMatrix(header, halfIndexMatrix, pixelVector);

  ofstream outStream(outName, ios::out | ios::binary);
  check((bool) outStream,
        "Error when opening \"" + outName + "\" for writing.");

  cout << "Saving \"" << outName << "\" ..." << endl;
  header.save(outStream);
  outStream.write(idBuffer, header.idLength);

  for (const Pixel& pixel : pixelVector) {
    pixel.save(outStream);
  }

  halfIndexMatrix.save(outStream);
  cout << "Done.";
}

void generateHalfIndexMatrix(Header& header,
                             const Matrix<Index> &originalIndexMatrix,
                             Matrix<Index>& halfIndexMatrix,
                             vector<Pixel>& pixelVector,
                             map<Pixel, Index>& pixelToIndexMap) {
  cout << "Resizing to: " <<header.width << "x"
       << header.height << " ..." << endl;

  for (int row = 0; row < halfIndexMatrix.height(); ++row) {
    for (int column = 0; column < halfIndexMatrix.width(); ++column) {
      Index index1 = originalIndexMatrix.get(2 * row, 2 * column),
            index2 = originalIndexMatrix.get(2 * row, (2 * column) + 1),
            index3 = originalIndexMatrix.get((2 * row) + 1, 2 * column),
            index4 = originalIndexMatrix.get((2 * row) + 1, (2 * column)+1);
      Pixel pixel1 = pixelVector[index1.index()],
            pixel2 = pixelVector[index2.index()],
            pixel3 = pixelVector[index3.index()],
            pixel4 = pixelVector[index4.index()];
      Pixel averagePixel =
        average(pixel1, average(pixel2, average(pixel3, pixel4)));

      if (pixelToIndexMap.count(averagePixel) > 0) {
        halfIndexMatrix.set(row, column, pixelToIndexMap[averagePixel]);
      }
      else {
        pixelToIndexMap[averagePixel] =
		  Index(header.bitsPerPixelOrIndex, (int)pixelVector.size());
		pixelVector.push_back(averagePixel);
        ++header.colorMapLength;
        halfIndexMatrix.set(row, column, pixelToIndexMap[averagePixel]);
      }
    }
  }

  cout << "Done." << endl;
}

void optimizeHalfIndexMatrix(Header& header, Matrix<Index>& halfIndexMatrix,
                             vector<Pixel>& pixelVector) {
  cout << "Optimizing image map ..." << endl;
  bool* markArray = new bool[pixelVector.size()];
  assert(markArray != nullptr);

  for (int index = 0; index < ((int) pixelVector.size()); ++index) {
    markArray[index] = false;
  }

  for (int row = 0; row < header.height; ++row) {
    for (int column = 0; column < header.width; ++column) {
      markArray[halfIndexMatrix.get(row, column).index()] = true;
    }
  }

  vector<Pixel> newPixelVector;
  map<Pixel, Index> newPixelToIndexMap;

  for (int index = 0; index < ((int) pixelVector.size()); ++index) {
    if (markArray[index]) {
      Pixel pixel = pixelVector[index];
      newPixelToIndexMap[pixel] =
		Index(header.bitsPerPixelOrIndex, (int) newPixelVector.size());
	  newPixelVector.push_back(pixel);
    }
  }

  for (int row = 0; row < header.height; ++row) {
    for (int column = 0; column < header.width; ++column) {
      Index oldIndex = halfIndexMatrix.get(row, column);
      Pixel pixel = pixelVector[oldIndex.index()];
      Index newIndex = newPixelToIndexMap[pixel];
      halfIndexMatrix.set(row, column, newIndex);
    }
  }

  header.colorMapLength = (short int)newPixelVector.size();
  cout << "Done: reduced " << pixelVector.size() << " entries to "
       << newPixelVector.size() << " entries." << endl;
  pixelVector = newPixelVector;
}

void check(bool test, const string& message) {
  if (!test) {
    cout << message << endl;
    exit(-1);
  }
}