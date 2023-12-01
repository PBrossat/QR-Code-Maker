import qrcode
import os
from PIL import Image
from colorama import init, Fore


# colors
white = (255, 255, 255) 
black = (0, 0, 0) 

init(autoreset=True) # colorama init

# function to verify the parameters
def verif_params(qr_link,box_size, border,qr_name, box_color, background_color, version,image, image_path):
    if not isinstance(qr_link, str):
        raise TypeError(f"{Fore.RED}qr_link must be a string")

    if not isinstance(box_size, int):
        raise TypeError(f"{Fore.RED}box_size must be an integer")
    else :
        if box_size < 1:
            raise ValueError(f"{Fore.RED}box_size must be greater than 0")
    
    if not isinstance(border, int):
        raise TypeError(f"{Fore.RED}border must be an integer")
    else :
        if border < 0:
            raise ValueError(f"{Fore.RED}border must be greater or equal to 0")
    
    if not isinstance(qr_name, str):
        raise TypeError(f"{Fore.RED}qr_name must be a string")
    
    if not isinstance(box_color, tuple):
        raise TypeError(f"{Fore.RED}box_color must be a tuple")
    else : 
        if len(box_color) != 3:
            raise ValueError(f"{Fore.RED}box_color must be a tuple of 3 elements")
        else : 
            # 0-255 for RGB
            if box_color[0] < 0 or box_color[0] > 255:
                raise ValueError(f"{Fore.RED}box color red value(R-.-.) must be between 0 and 255")
            if box_color[1] < 0 or box_color[1] > 255:
                raise ValueError(f"{Fore.RED}box color green value(.-G-.) must be between 0 and 255")
            if box_color[2] < 0 or box_color[2] > 255:
                raise ValueError(f"{Fore.RED}box color blue value(.-.-B) must be between 0 and 255")
            
    if not isinstance(background_color, tuple):
        raise TypeError(f"{Fore.RED}background_color must be a tuple")
    else :
        if len(background_color) != 3:
            raise ValueError(f"{Fore.RED}background_color must be a tuple of 3 elements")
        else : 
            # 0-255 for RGB
            if background_color[0] < 0 or background_color[0] > 255:
                raise ValueError(f"{Fore.RED}background color red value(R-.-.) must be between 0 and 255")
            if background_color[1] < 0 or background_color[1] > 255:
                raise ValueError(f"{Fore.RED}background color green value(.-G-.) must be between 0 and 255")
            if background_color[2] < 0 or background_color[2] > 255:
                raise ValueError(f"{Fore.RED}background color blue value(.-.-B) must be between 0 and 255")
    
    if not isinstance(version, int):
        raise TypeError(f"{Fore.RED}version must be an integer")
    else : 
        if version < 1 or version > 40:
            raise ValueError(f"{Fore.RED}version must be between 1 and 40")
    
    # If image is True we check the image_path parameter
    if image:
        if not isinstance(image_path, str):
            raise TypeError(f"{Fore.RED}image_path must be a string")

        if not os.path.exists(image_path):
            raise ValueError(f"{Fore.RED}image_path must be a valid path")
    


def create_qr(qr_link,
            box_size, 
            border,
            qr_name, 
            box_color, 
            background_color, 
            version,
            image,
            image_path):
    
    """
    Function to create a QR code with the parameters given.
    :param qr_link: link to encode
    :param box_size: size of the box (in pixels)
    :param border: white border around the QR code
    :param qr_name: name of the QR code file
    :param box_color: color of the box
    :param background_color: color of the background
    :param version: version of the QR code
    :param image: boolean to add an image in the QR code
    :param image_path: path of the image to add in the QR code
    """
    
    # Verifications of the parameters
    try:
        verif_params(qr_link,box_size, border,qr_name, box_color, background_color, version, image, image_path)
    except TypeError as e:
        print(f"Error: {e}")
        return

    
    if image:
        image_qr = Image.open(image_path)

    qr = qrcode.QRCode(
        version=version, # the bigger the version, the bigger the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_M, 
        box_size=box_size, # box_size*box_size pixels per box
        border=border, # border around the QR code
    )


    qr.add_data(qr_link) # URL to encode 
    qr.make(fit=True) # fit the QR code to the data
    qr_code = qr.make_image(fill_color=box_color, back_color=background_color) # create the QR code image

    # If image is True, we add the image in the QR code
    if image :
        # resize the image to fit in the QR code
        image_qr = image_qr.resize((qr_code.size[0]//5, qr_code.size[1]//5))
        # position of the image in the QR code (middle of the QR code)
        pos = ((qr_code.size[0] - image_qr.size[0]) // 2, (qr_code.size[1] - image_qr.size[1]) // 2)
        # paste the image in the QR code    
        qr_code.paste(image_qr, pos)

    qr_code.save("QR_Code_image/" + qr_name) # save the image
    print("QR code saved as {}".format(qr_name))


def main():
    qr_link = input("Entrez le lien du QR code : ")
    box_size = int(input("Entrez la taille d'un pixel du QR code' (en pixels) : "))

    border_choice = input("Voulez-vous entrer une bordure autour du QR code (O/N) ? : ").lower()
    if border_choice.strip().lower() == 'o':
        border = int(input("Entrez la taille de la bordure autour du QR code : "))
    else:
        border = 1

    qr_name = input("Entrez le nom du fichier QR code : ")

    box_color_choice = input("Voulez-vous entrer une couleur de pixel (O/N) ? : ").lower()
    if box_color_choice.strip().lower() == 'o':
        box_color = tuple(map(int, input("Entrez la couleur du pixel (R G B séparés par des espaces) : ").split()))
    else:
        box_color = black

    background_color_choice = input("Voulez-vous entrer une couleur d'arrière-plan (O/N) ? : ").lower()
    if background_color_choice.strip().lower() == 'o':
        background_color = tuple(map(int, input("Entrez la couleur de l'arrière-plan (R G B séparés par des espaces) : ").split()))
    else:
        background_color = white

    version_choice = input("Voulez-vous entrer une précision (plus la précision est grande plus le qr code sera grand) (O/N) ? : ").lower()
    if version_choice.strip().lower() == 'o':
        version = int(input("Entrez la taille du QR code : "))
    else:
        version = 3  

    image_choice = input("Voulez-vous ajouter une image au QR code (O/N) ? : ").lower()
    if image_choice.strip().lower() == 'o':
        image = True
        image_path = input("Entrez le chemin de l'image à ajouter : ")
    else:
        image = False
        image_path = ""  # Pas de chemin d'image si image est False

    create_qr(qr_link, box_size, border, qr_name, box_color, background_color, version, image, image_path)

if __name__ == "__main__":
    main()