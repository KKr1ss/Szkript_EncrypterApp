from cryptography.fernet import Fernet
import EncryptionFileHandler

key = Fernet.generate_key()

filePath = ""
fileData = ""


def setFile(path):
    EncryptionFileHandler.filePath = path
    try:
        file = open(EncryptionFileHandler.filePath, 'r')
        EncryptionFileHandler.fileData = file.read()
    finally:
        file.close()


def createFile(encrypted):
    newFileData = decrypt() if encrypted else encrypt()
    newFilePath = filePath[:len(filePath) - 10 ] if encrypted else filePath + ".encripted"
    file = open(newFilePath, 'w')
    file.write(newFileData.decode())
    file.close()
    return newFilePath


def encrypt():
    encryptedMessage = Fernet(key).encrypt(fileData.encode())
    return encryptedMessage


def decrypt():
    decryptedMessage = Fernet(key).decrypt(fileData)
    return decryptedMessage