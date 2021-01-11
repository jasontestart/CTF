#!/usr/bin/python3
import subprocess
import shlex
import os
import io
import PyPDF2

KEY_LENGTH = 8
state = 0

# hint from https://rosettacode.org/wiki/Linear_congruential_generator#Python
def super_secure_random():
    global state
    r = 214013*state + 2531011
    state = r
    return r >> 16 & 32767

def super_secure_srand(seed):
    global state
    state = seed

def generate_key(seed):
    global KEY_LENGTH
    super_secure_srand(seed)
    key = []
    for i in range(0,KEY_LENGTH):
        this_byte = super_secure_random() & 0x0FF
        key.append(this_byte)
    return key

def print_hex(key):
    out_string = ''
    hex_part = ''
    for b in key:
        if not b:
            hex_part = '00'
        elif b < 16:
            hex_part = f'0{str(hex(b))[2:]}'
        else:
            hex_part = str(hex(b))[2:]
        out_string += hex_part
    return f'{out_string}'

start_time = 1575658800
end_time = 1575666000
seed = start_time
enc_file_path = 'ElfUResearchLabsSuperSledOMaticQuickStartGuideV1.2.pdf.enc'
dec_file_path = enc_file_path.replace('.enc','')
dev_null = open(os.devnull, 'wb')
for seed in range(start_time, end_time + 1):
    thiskey = generate_key(int(seed))
    thishex = print_hex(thiskey)
    print(f"Trying seed {seed} with key {thishex}")
    openssl_cmd = f'openssl enc -des-cbc -d -K {thishex} -iv 0000000000000000 -in {enc_file_path}'
    args = shlex.split(openssl_cmd)
    openssl_result = subprocess.run(args, stdout=subprocess.PIPE,stderr=dev_null)
    working_stream=io.BytesIO(openssl_result.stdout)
    if not openssl_result.returncode:
        try:
            PyPDF2.PdfFileReader(working_stream)
        except PyPDF2.utils.PdfReadError:
            continue
        else:
            outfile = open(dec_file_path,'wb+')
            outfile.write(openssl_result.stdout)
            outfile.close()
            print(f'Success with seed {seed} and key {thishex}')
            print(f'Decrypted file saved to {dec_file_path}')
            break
