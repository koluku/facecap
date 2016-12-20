# FACECAP

Macbookのフロントカメラで人間の顔をキャプチャするPythonアプリです。

## Requirements

- Python 3.5.2
- OpenCV3

## Usage

プログラムを実行すると3秒に一回撮影します。その撮影された中に顔が検出されるとfacesフォルダに顔だけが切り抜かれた画像を出力します。

```
python cap.py
```

Qキーを押すことでプログラムが終了します。

## License

[MIT License](LICENSE)

## Author

[koluku](https://github.com/koluku)
