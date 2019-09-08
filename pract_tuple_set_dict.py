
total_student = input("How many are students? ");


total_student = int(total_student);
print(total_student, type(total_student));

i = int(0);
full_std = list();

while (i < total_student) :
	name = input("Name : ");
	score = input("Score : ");

	print("Name = ", name , "Score = " , score);

	score = int(score);
	entry = (name, score);

	print(entry);

	full_std.append(entry);

	i += 1;


print("full_student = ");
print( full_std );

dict_full_std = dict(full_std);
print( dict_full_std );

retry = True;

while (retry) :
	sr_name = input("Input name what you want : ");

	retry = sr_name not in dict_full_std;	


print(sr_name , " -- score = ", dict_full_std[sr_name]);


print("End of program");
