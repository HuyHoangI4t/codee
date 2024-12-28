#include <iostream>
#include <opencv2/opencv.hpp>

const std::string ASCII_CHARS = "@%#*+=-:. "; // Các ký t? ASCII, t? ??m ??n nh?t.

char getASCIIFromIntensity(int intensity) {
    int index = (intensity * (ASCII_CHARS.size() - 1)) / 255;
    return ASCII_CHARS[index];
}

void printImageAsASCII(const cv::Mat& img) {
    for (int i = 0; i < img.rows; ++i) {
        for (int j = 0; j < img.cols; ++j) {
            int intensity = img.at<uchar>(i, j);
            std::cout << getASCIIFromIntensity(intensity);
        }
        std::cout << std::endl;
    }
}

int main() {
    std::string imagePath;
    std::cout << "Nhap duong dan anh: ";
    std::cin >> imagePath;

    cv::Mat image = cv::imread(imagePath, cv::IMREAD_GRAYSCALE); // Chuy?n ?nh v? grayscale.
    if (image.empty()) {
        std::cerr << "Khong the mo anh tai duong dan: " << imagePath << std::endl;
        return -1;
    }

    // Resize ?nh ?? phù h?p hi?n th? ASCII
    cv::Mat resizedImage;
    const int newWidth = 80; // Chi?u r?ng mong mu?n.
    int newHeight = (image.rows * newWidth) / image.cols;
    cv::resize(image, resizedImage, cv::Size(newWidth, newHeight));

    printImageAsASCII(resizedImage);

    return 0;
}
