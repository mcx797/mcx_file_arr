import os
import sys

from PyQt5.QtCore import Qt, QTranslator
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import FluentTranslator, QConfig, qconfig
from app.common.config import Config

from app.view.main_window import MainWindow


if __name__ == '__main__':
    # enable dpi scale
    cfg = Config()
    qconfig.load('app/config/config.json', cfg)
    if cfg.get(cfg.dpiScale) == "Auto":
        QApplication.setHighDpiScaleFactorRoundingPolicy(
            Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    else:
        os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
        os.environ["QT_SCALE_FACTOR"] = str(cfg.get(cfg.dpiScale))
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    # create application
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)

    # internationalization

    locale = cfg.get(cfg.language).value
    translator = FluentTranslator(locale)
    galleryTranslator = QTranslator()
    galleryTranslator.load(locale, "gallery", ".", "app/resource/i18n")

    app.installTranslator(translator)
    app.installTranslator(galleryTranslator)

    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()