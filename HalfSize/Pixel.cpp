// Stefan Björnander

#include <fstream>
#include <cassert>
using namespace std;
#include "Pixel.h"

Pixel::Pixel(int bitsPerPixel /* = 0 */)
 :m_bitsPerPixel(bitsPerPixel),
  m_red(0),
  m_green(0),
  m_blue(0),
  m_alpha(0) {
  // Empty.
}

Pixel::Pixel(const Pixel& pixel)
 :m_bitsPerPixel(pixel.m_bitsPerPixel),
  m_red(pixel.m_red),
  m_green(pixel.m_green),
  m_blue(pixel.m_blue),
  m_alpha(pixel.m_alpha) {
 // Empty.
}

Pixel& Pixel::operator=(const Pixel& pixel) {
  m_bitsPerPixel = pixel.m_bitsPerPixel;
  m_red = pixel.m_red;
  m_green = pixel.m_green;
  m_blue = pixel.m_blue;
  m_alpha = pixel.m_alpha;
  return *this;
}

bool Pixel::operator==(const Pixel& pixel) const {
  assert(m_bitsPerPixel == pixel.m_bitsPerPixel);
  return (m_red == pixel.m_red) &&
         (m_green == pixel.m_green) &&
         (m_blue == pixel.m_blue) &&
         (m_alpha == pixel.m_alpha);
}

bool Pixel::operator<(const Pixel& pixel) const {
  assert(m_bitsPerPixel == pixel.m_bitsPerPixel);
  int thisWord = (((int) m_alpha) << 24) |
                          (((int) m_blue) << 16) |
                          (((int) m_green) << 8) |
                           ((int) m_red),
               pixelWord = (((int) pixel.m_alpha) << 24) |
                           (((int) pixel.m_blue) << 16) |
                           (((int) pixel.m_green) << 8) |
                            ((int) pixel.m_red);
  return (thisWord < pixelWord);
}

void Pixel::load(int bitsPerPixelOrIndex, ifstream& inStream) {
  switch (m_bitsPerPixel = bitsPerPixelOrIndex) {
    case 8:
      inStream.read((char*) &m_alpha, sizeof m_alpha);
      break;

    case 16: {
        short int word;
        inStream.read((char*) &word, sizeof word);

        m_red = (char) (word & 0x001F);
        m_green = (char) ((word >> 5) & 0x001F);
        m_blue = (char) ((word >> 10) & 0x001F);
        m_alpha = (char) ((word >> 15) & 0x0001);
      }
      break;

    case 24:
      inStream.read((char*) &m_red, sizeof m_red);
      inStream.read((char*) &m_green, sizeof m_blue);
      inStream.read((char*) &m_blue, sizeof m_green);
      m_alpha = 0;
      break;

    case 32:
      inStream.read((char*) &m_red, sizeof m_red);
      inStream.read((char*) &m_green, sizeof m_blue);
      inStream.read((char*) &m_blue, sizeof m_green);
      inStream.read((char*) &m_alpha, sizeof m_alpha);
      break;
  }
}

void Pixel::save(ofstream& outStream) const {
  switch (m_bitsPerPixel) {
    case 8:
      outStream.write((char*) &m_alpha, sizeof m_alpha);
      break;

    case 16: {
        short int word = (((short int) m_alpha) << 15) |
                         (((short int) m_blue) << 10) |
                         (((short int) m_green) << 5) |
                          ((short int) m_red);
        outStream.write((char*) &word, sizeof word);
      }
      break;

    case 24:
      outStream.write((char*) &m_red, sizeof m_red);
      outStream.write((char*) &m_green, sizeof m_blue);
      outStream.write((char*) &m_blue, sizeof m_green);
      break;

    case 32:
      outStream.write((char*) &m_red, sizeof m_red);
      outStream.write((char*) &m_green, sizeof m_blue);
      outStream.write((char*) &m_blue, sizeof m_green);
      outStream.write((char*) &m_alpha, sizeof m_alpha);
      break;
  }
}

Pixel average(const Pixel& leftPixel, const Pixel& rightPixel) {
  assert(leftPixel.m_bitsPerPixel == rightPixel.m_bitsPerPixel);
  Pixel resultPixel;
  resultPixel.m_bitsPerPixel = leftPixel.m_bitsPerPixel;

  switch (resultPixel.m_bitsPerPixel) {
    case 8:
      resultPixel.m_alpha = (leftPixel.m_alpha + rightPixel.m_alpha) / 2;
      break;

    case 16:
    case 24:
    case 32:
      resultPixel.m_red = (leftPixel.m_red + rightPixel.m_red) / 2;
      resultPixel.m_green = (leftPixel.m_green + rightPixel.m_green) / 2;
      resultPixel.m_blue = (leftPixel.m_blue + rightPixel.m_blue) / 2;
      resultPixel.m_alpha = (leftPixel.m_alpha + rightPixel.m_alpha) / 2;
      break;
  }

  return resultPixel;
}
