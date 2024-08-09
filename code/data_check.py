import os
import numpy as np
from PIL import Image

def get_folders_list(camera_path, label_path):
    #otteniamo il numero di file di entrabe le cartelle
    print("Ottengo la lista di nomi dei file ...")
    if os.path.exists(camera_path):
        camera_imgs_list_names = os.listdir(camera_path)   #contengono i nomi delle singole immagini
        print("Lista nomi immagini popolata")
    else: raise Exception("Errore: cartella immagini non trovata")
    if os.path.exists(label_path):
        label_imgs_list_names = os.listdir(label_path)
        print("Lista nomi labels popolata")
    else: raise Exception("Errore: cartella label non trovata")
    #verifichiamo che il numero di immagini sia lo stesso
    if len(camera_imgs_list_names) == len(label_imgs_list_names):
        print("Il numero di immagini è lo stesso (",len(camera_imgs_list_names),")")
    else:
        raise Exception("Il numero di immagini è diverso")

    #verifichiamo che i nomi dei file siano uguali in entrambe le cartelle
    #immagine camera: 20180807145028_camera_frontcenter_000000091.png
    #immagine label: 20180807145028_label_frontcenter_000000091.png

    camera_imgs_list_names.sort()
    label_imgs_list_names.sort()
    for i in range(len(camera_imgs_list_names)):
        if camera_imgs_list_names[i].replace("camera", "") != label_imgs_list_names[i].replace("label", ""):
            raise Exception("I nomi dei file sono diversi")

    print("I nomi dei file sono uguali")
    print("\n EVERYTHING OK")
    return camera_imgs_list_names, label_imgs_list_names

def check_label(label_path, label_name, colori_classi_label_hex):
    with Image.open(label_path + label_name) as label:
        label = np.array(label)
        hoes_label = np.zeros((label.shape[0], label.shape[1], 3))
        pixels_sbagliati = 0

        for i in range(label.shape[0]):
            for j in range(label.shape[1]):
                colore_pixel_corrente = "#%02x%02x%02x" % (label[i, j, 0], label[i, j, 1], label[i, j, 2])
                if colore_pixel_corrente in colori_classi_label_hex.keys():
                    hoes_label[i, j, :] = 1
                else:
                    hoes_label[i, j, :] = 0
                    pixels_sbagliati += 1

        print("numero di buchi: ", pixels_sbagliati)
        print("\n EVERYTHING OK")