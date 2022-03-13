// Stefan Björnander

class Pixel {
  public:
    Pixel(int bitsPerPixel = 0);
    Pixel(const Pixel& pixel);
    Pixel& operator=(const Pixel& pixel);

    bool operator==(const Pixel& pixel) const;
    bool operator<(const Pixel& pixel) const;

    void load(int bitsPerPixelOrIndex, ifstream& inStream);
    void save(ofstream& outStream) const;

    friend Pixel average(const Pixel& leftPixel, const Pixel& rightPixel);

  public:
    int m_bitsPerPixel;
    char m_red, m_green, m_blue, m_alpha;
};