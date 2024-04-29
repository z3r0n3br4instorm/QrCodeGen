import qrcode
import os
def generate_qr_code(link, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(os.path.join("QRs", file_name))

if __name__ == "__main__":
    LinksFile = open("Links.txt", "r")
    for link in LinksFile:
        file_name = link.split("/")[-1].strip() + ".png"
        generate_qr_code(link, file_name)
    # Zip The Folder QRs
    os.system("zip -r QRs.zip QRs")
    print("QR codes generated successfully!")