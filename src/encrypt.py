import os
import struct
import hashlib
import Crypto.Random as Random
from Crypto.Cipher import AES



class EncryptTransactions:
    def encrypt_file(self, file_name, key):
        chunk_size = 64 * 1024
        output_file = os.path.join(os.path.dirname(file_name), "encrypted" + os.path.basename(file_name))
        IV = Random.new().read(AES.block_size)
        encryptor = AES.new(key, AES.MODE_CBC, IV)
        
        with open(file_name, 'rb') as input_file, open(output_file, 'wb') as output_file:
            output_file.write(struct.pack('<Q', os.path.getsize(file_name)))
            output_file.write(IV)
            
            while True:
                chunk = input_file.read(chunk_size)
                
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b'\0' * (16 - (len(chunk) % 16))
                    
                output_file.write(encryptor.encrypt(chunk))
                
    def decrypt_file(self, file_name, key):
        chunk_size = 64 * 1024
        output_file = file_name.replace('encrypted', 'decrypted')
        
        with open(file_name, 'rb') as input_file:
            orig_size = struct.unpack('<Q', input_file.read(struct.calcsize('Q')))[0]
            IV = input_file.read(AES.block_size)
            decryptor = AES.new(key, AES.MODE_CBC, IV)
            
            with open(output_file, 'wb') as output_file:
                while True:
                    chunk = input_file.read(chunk_size)
                    
                    if len(chunk) == 0:
                        break
                        
                    output_file.write(decryptor.decrypt(chunk))
                    
                output_file.truncate(orig_size)
                
    def get_key(self, password):
        hasher = hashlib.sha256()
        hasher.update(password.encode('utf-8'))
        return hasher.digest()
    
    def get_password(self):
        return input("Password: ")
    
    def password_check(self, password):
        contains_big_char = False
        contains_small_char = False
        contains_number = False
        
        if len(password) < 8:
            return False
        
        for char in password:
            if char.isdigit():
                contains_number = True
            elif char.isupper():
                contains_big_char = True
            elif char.islower():
                contains_small_char = True
                
        if contains_big_char and contains_small_char and contains_number:
            return True
        else:
            return False
