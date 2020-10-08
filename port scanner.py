import socket
import sys
import subprocess
from datetime import datetime

subprocess.call("clear")
print ("/////////     //////////////  ///////////  ///////////////        ///////////     /////////////   //\\               //\\            //")
print ("//     //    //          //  //      ///        //               ///             //              //  \\             //  \\          // ")
print ("//     //   //          //  //      ///        //               ///             //              //    \\           //    \\        //  ")
print ("/////////  //          //  ///////////        //               /////////////   //              //::::::\\         //      \\      //   ")
print ("//        //          //  //        \\        //                         ///   //              //        \\       //        \\    //    ")
print ("//       //          //  //          \\      //                         ///   //              //          \\     //          \\  //     ")
print ("//      //////////////  //            \\    //                 ///////////   //////////////  //            \\   //            \\//      ")

print (" ")
print ("                      mehrdad sepehr                                                                                                    ")
print (" ")

remoteserver_IP = input("enter IP address : ")
remoteserver_address = socket.gethostbyname(remoteserver_IP)
print ("-"*40)
print ("pleas wait : ", remoteserver_address)
print ("-"*40)
print ("Help : ")
print ("A_   press ctrl + c stup work")
print ("-"*40)
t1 = datetime.now()
try:
    for port in range (1, 9999):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        end = sock.connect_ex((remoteserver_address, port))
        if end == 0:
            print("port {} :                  open".format(port))


except KeyboardInterrupt:
    print("you're press ctrl + c :|")
    sys.exit()
except socket.gaierror:
    print("I can't conecting the IP address")
except socket.error:
    print("socket error conecting")
t2 = datetime.now()
t3 = t2-t1
print ("scan finisht in ", t3)
