def makeTextFile(name, content):
    file = open(f"../frontend/src/transcripts/{name}.txt","w",encoding="utf-8")
    
    file.write(f"{name} Transcript:\n")
    file.write(content)
    file.close()
