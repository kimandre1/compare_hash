import hashlib, argparse, os

#Checks hash on file
def sha256sum(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, 'rb') as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

#Stores hash in filename.hash
def save_hash(filename):
    with open(f"{filename}.hash", "w") as fp:
        fp.write(sha256sum(filename))
        print(f"sum saved at {filename}.hash")

#Compares checksum in filename.hash to current hash value
def compare_hash(filename):
    if os.path.exists(filename):
        print("File detected!")
        with open(f"{filename}.hash") as f:
            oldhash = f.read()
        if sha256sum(filename) == oldhash:
            print("checksum is the same!")
        else:
            print("file isn't the same anymore!")
    else:
        print("file isn't here anymore!")

parser = argparse.ArgumentParser(description="Store, check and compare sha256 value of a given file. use -h for instructions.")
parser.add_argument("--compare", help='add to compare files, usage: --compare "filename1" "filename"', action ="store_true")
parser.add_argument("--file", help="input filename, required field", required=True)
parser.add_argument("--store", help="add to store file hash to filename.hash", action ="store_true")
args = parser.parse_args()

if args.compare == True:
    compare_hash(args.file)

if args.store == True:
    save_hash(args.file)   
    
if args.compare == args.store == True:
    print("There is no point comparing and saving at the same time! please remove one argument!")