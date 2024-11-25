import os
import re
import subprocess
import requests
import shutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class SevenZipUpdater(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("7-Zip Güncelleme Kontrolü")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #2C3E50; color: #ECF0F1;")

        # Pencere İkonu
        self.setWindowIcon(QIcon("7zip.png"))

        # Widget'lar
        self.title_label = QLabel("7-Zip Güncelleme Kontrolü")
        self.title_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)

        self.status_label = QLabel("Durum: Hazır")
        self.status_label.setFont(QFont("Arial", 12))
        self.status_label.setAlignment(Qt.AlignCenter)

        self.check_button = QPushButton("Sürüm Kontrolü Yap")
        self.check_button.setFont(QFont("Arial", 12))
        self.check_button.setStyleSheet("background-color: #3498DB; color: white; border-radius: 5px; padding: 10px;")
        self.check_button.clicked.connect(self.check_versions)

        self.update_button = QPushButton("Güncellemeyi İndir ve Kur")
        self.update_button.setFont(QFont("Arial", 12))
        self.update_button.setStyleSheet("background-color: #2ECC71; color: white; border-radius: 5px; padding: 10px;")
        self.update_button.clicked.connect(self.update_7zip)
        self.update_button.setDisabled(True)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.status_label)
        layout.addWidget(self.check_button)
        layout.addWidget(self.update_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Sürüm bilgileri
        self.installed_version = None
        self.latest_version = None

    def get_installed_version(self):
        seven_zip_path = r"C:\Program Files\7-Zip\7z.exe"
        if os.path.exists(seven_zip_path):
            try:
                result = subprocess.run([seven_zip_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                version_match = re.search(r'7-Zip (\d+\.\d+)', result.stdout)
                if version_match:
                    return version_match.group(1)
            except Exception as e:
                print(f"Hata: {e}")
        return None

    def get_latest_version(self):
        url = "https://www.7-zip.org/"
        response = requests.get(url)
        if response.status_code == 200:
            version_match = re.search(r'Download 7-Zip ([\d\.]+)', response.text)
            if version_match:
                return version_match.group(1)
        return None

    def download_latest_version(self, version):
        download_url = f"https://www.7-zip.org/a/7z{version.replace('.', '')}-x64.exe"
        response = requests.get(download_url, stream=True)
        if response.status_code == 200:
            file_path = f"7z{version}-setup.exe"
            with open(file_path, "wb") as file:
                shutil.copyfileobj(response.raw, file)
            return file_path
        return None

    def install_7zip(self, installer_path):
        try:
            subprocess.run([installer_path, '/S'], check=True)
            QMessageBox.information(self, "Başarı", "7-Zip başarıyla yüklendi!")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Yükleme sırasında hata oluştu: {e}")

    def check_versions(self):
        self.status_label.setText("Durum: Sürüm kontrolü yapılıyor...")
        QApplication.processEvents()  # Arayüzün donmasını engeller

        self.installed_version = self.get_installed_version()
        self.latest_version = self.get_latest_version()

        if self.installed_version:
            self.status_label.setText(f"Mevcut sürüm: {self.installed_version}")
        else:
            self.status_label.setText("7-Zip sistemde yüklü değil.")

        if self.latest_version:
            if self.installed_version == self.latest_version:
                QMessageBox.information(self, "Bilgi", "Sisteminizde en güncel sürüm yüklü.")
                self.update_button.setDisabled(True)
            else:
                QMessageBox.information(self, "Güncelleme Mevcut", f"Yeni bir sürüm var: {self.latest_version}")
                self.update_button.setDisabled(False)
        else:
            QMessageBox.warning(self, "Hata", "Güncel sürüm bilgisi alınamadı.")
            self.update_button.setDisabled(True)

    def update_7zip(self):
        if self.latest_version:
            self.status_label.setText("Durum: Güncelleme indiriliyor...")
            QApplication.processEvents()  # Arayüzün donmasını engeller

            installer_path = self.download_latest_version(self.latest_version)
            if installer_path:
                self.status_label.setText("Durum: Kurulum başlatılıyor...")
                self.install_7zip(installer_path)
                os.remove(installer_path)  # Kurulum dosyasını sil
            else:
                QMessageBox.critical(self, "Hata", "İndirme başarısız oldu.")
            self.status_label.setText("Durum: Hazır")
        else:
            QMessageBox.warning(self, "Hata", "Güncelleme bilgisi alınamadı.")

if __name__ == "__main__":
    app = QApplication([])
    window = SevenZipUpdater()
    window.show()
    app.exec()
