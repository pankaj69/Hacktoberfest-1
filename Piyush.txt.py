#ERROR: User_ID=201 , Reason ="Time_OUT" , error_code=0x02
f=open("Text1.txt", 'r')
#file=f.read()
for i in range(1,10):
    line=f.readline()
    ch=input("Y/N")
    if ch=='Y':
        print(line)



"""
$servername = "server"
$user = "username"
$password = "password" 

$db=mysqli_connect($servername, $user, $password)
if (!db){
die(echo "DATABASE NOT CONNECTED)
}

else{
echo "DATABASE CONNECTED"
}


$sql = "SELECT * from User_table where name='PIYUSH' "

mysql_query($db, $sql);
$myDb=mysql_fetch_array($sql)
echo $sql;

$arr=array("A","Z","B")
arr.sort()
echo $arr;

$sql
"""