import dropbox

class transferData:
    def __init__(self,accessToken):
        self.accessToken=accessToken

    def uploadFile(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.accessToken)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    accessToken='sl.AtoYsnyzCAxrPpe1IeEIneoITRwNseqMwh75V9PWhwHty8uMhoiYYS1G3ziJGh4HdBWtgx-3FhYUcdi2Vl78FKH8frgFLLtoQwHJR3MsmPR9kCTa9CwhBIBCe7jF8YV-h8zfAAa8m30'
    transferData_obj=transferData(accessToken)
    file_from=input("Enter the file path to tranfer: ")
    file_to=input("Enter the path to upload in dropbox: ")
    transferData_obj.uploadFile(file_from,file_to)
    print("File has has been successfully transferred !")

main()