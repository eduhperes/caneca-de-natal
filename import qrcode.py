import qrcode

url = "https://eduhperes.github.io/caneca-de-natal/"
qr = qrcode.make(url)
qr.save("meu_qrcode.png")
print("QR Code gerado com sucesso!")
