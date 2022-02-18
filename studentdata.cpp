#include <stdio.h>
#include <string.h>
#include <stdlib.h>


struct node 
{
    char name[100];
    int  math,m;
    int science,s;
    int english,e;
    int sum;
    char grade[2];	
    struct node *next;
};

struct node *root = NULL;

void showMenu()
{
	printf("\n");

    printf("1 - Add Data\n");
    printf("2 - Delete Data\n");
    printf("3 - Display Data\n");
    printf("4 - Search Data\n");
    printf("5 - Exit\n\n");
    printf("choice -> ");
}

int getChoice()
{
    int choice;
    scanf("%d", &choice);
    printf("\n\n");
    return choice;
}

void addData()
{
    struct node *data = (struct node*) malloc(sizeof(struct node));
    printf("Name: ");
    scanf("%s", &data->name);
    printf("math:");
    scanf("%d", &data->math);
    printf("science:");
    scanf("%d", &data->science);
    printf("english:");
    scanf("%d", &data->english);
    data->sum = data->math + data->science +data->english;
    if (data->sum <= 49){
		strcpy(data->grade, "C");
	}else if(data->sum >= 50||data->sum <= 69){
		strcpy(data->grade, "B");
	}else if(data->sum >= 70||data->sum <= 100){
		strcpy(data->grade, "A");	
	}
        printf("Name      %s\n", data->name);
        printf("  math    %d\n", data->math);
        printf("  science %d\n", data->science);
        printf("  english %d\n", data->english);
        printf("Sum       %d\n", data->sum);
        printf("grade     %s\n", data->grade);
    if(root == NULL){
        data->next = NULL;
    }else{
        data->next = root;
    }
    root = data;
}

void displayData()
{
    struct node *ptr = root;
    while(ptr != NULL){
        printf("Name      %s\n", ptr->name);
        printf("  math    %d\n", ptr->math);
        printf("  science %d\n", ptr->science);
        printf("  english %d\n", ptr->english);
        printf("Sum       %d\n",ptr->sum);
        printf("grade       %s\n",ptr->grade);
        ptr = ptr->next;
    }
    printf("\n");
}
void searchdata()
{
	char grade[100];
	struct node *ptr = root;
	printf("Input Group to Search -> ");
	scanf("%s",&grade);
	while(ptr != NULL){
		if(strcmp(ptr->grade ,grade)==0){
			break;
		}
		ptr = ptr->next;	
	}
	if(ptr != NULL){
		printf("Name      %s\n", ptr->name);
        printf("  math    %d\n", ptr->math);
        printf("  science %d\n", ptr->science);
        printf("  english %d\n", ptr->english);
        printf("Sum       %d\n", ptr->sum);
        printf("grade     %s\n", ptr->grade);
	}	
	else{
		printf("=====Not Found=====\n\n");
	}		
}
void deleteData()
{
    char name[100];
    printf("Name to delete -> ");
    scanf("%s", &name);
    
    struct node *ptr = root;
    struct node *last = root;
    
    while(ptr != NULL){
        if(strcmp(ptr->name, name)==0){
            break;
            
        }
        last = ptr;
        ptr = ptr->next;
    }
    if(ptr==NULL){
        printf("=====Data not found=====\n\n");
        return;
    }else{
        if(ptr==last){
            if(ptr->next==NULL){
                root = NULL;
                free(ptr);
                return;
            }
            root = ptr->next;
            free(ptr);
            return;
        }
        last->next = ptr->next;
        free(ptr);
        return;
    }
}

int main()
{
   for(;;){
       showMenu();
       int choice = getChoice();
       switch(choice){
            case 1:
                addData();
                break;
            case 2:
                deleteData();
                break;
            case 3:
                displayData();
                break;
            case 4:
                searchdata();
                break;
            case 5:
				return 0;    
                
       }
   }
   return 0;
}
