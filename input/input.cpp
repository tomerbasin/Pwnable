#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>
#include <string.h>
#include <fcntl.h> 
#include <iostream> 
#include <sys/socket.h> 
#include <arpa/inet.h> 
using namespace std;
#define READ 0
#define WRITE 1
#define ERR 2
int main()
{
	int pid;
	int fd1[2];
	int fd2[2];
	pipe(fd1);
	pipe(fd2);
	char * argv_list[101] = {"/home/input2/input"};
	char input[40];
	for (int i = 1; i < 101; i++)
	{
		argv_list[i] = "1";
	}
	argv_list[65] = "\x00";
	argv_list[66] = "\x20\x0a\x0d";
	argv_list[67] = "\x35\x30\x30\x32";
	argv_list[100] = NULL;
	
	
	pid = fork();
	if (pid == 0)
	{
		write(fd1[1], "\x00\x0a\x00\xff", 4);
		write(fd2[1], "\x00\x0a\x02\xff", 4);
		dup2(fd1[READ], READ);
		dup2(fd2[READ], ERR);
		setenv("\xde\xad\xbe\xef", "\xca\xfe\xba\xbe", 0);
		FILE* fp = fopen("\x0a", "w");
		fwrite("\x00\x00\x00\x00",4,4,fp);
		fclose(fp);
		execv("/home/input2/input", argv_list);
	}
	else
	{
		sleep(1);
		int sock = 0, valread;
		struct sockaddr_in serv_addr;
		char *buffer = "\xde\xad\xbe\xef";
		if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
		{
			printf("\n Socket creation error \n");
			return -1;
		}

		serv_addr.sin_family = AF_INET;
		serv_addr.sin_port = htons(5002);

		// Convert IPv4 and IPv6 addresses from text to binary form 
		if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0)
		{
			printf("\nInvalid address/ Address not supported \n");
			return -1;
		}

		if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
		{
			printf("\nConnection Failed \n");
			return -1;
		}
		send(sock, buffer, strlen(buffer), 0);
	}
	
	return 1;
}
