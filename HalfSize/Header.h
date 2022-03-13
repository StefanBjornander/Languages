// Stefan Björnander

struct Header {
  void load(ifstream& inStream);
  void save(ofstream& outStream) const;

  char idLength;
  char colorMapType;
  char dataTypeCode;
  short int colorMapOrigin;
  short int colorMapLength;
  char colorMapDepth;
  short int xOrigin;
  short int yOrigin;
  short int width;
  short int height;
  char bitsPerPixelOrIndex;
  char imageDescriptor;
};