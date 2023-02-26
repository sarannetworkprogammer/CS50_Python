def main():
    filename = input("Filename: ").strip().lower().split(".")

    a = len(filename) - 1

    if filename[a] in ["gif","png"]:
        print("image/"+filename[a])
    elif filename[a] in ["jpg","jpeg"]:
        print("image/jpeg")

    elif filename[a] == "pdf":
        print("application/"+filename[a])
    elif filename[a] == "txt":
        print("text/"+filename[0])
    elif filename[a] == "zip":
        print("application/"+filename[a])
    else:
        print("application/octet-stream")

main()