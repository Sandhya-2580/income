class income:
    def __init__(self,name,phone_no,email):
        self.name=[name]
        self.email=[email]
        self.phone_no=[phone_no]
    def add(self,name,phone_no,email):
        if name not in self.name:
            self.name.append(name)
        if phone_no not in self.phone_no:
            self.phone_no.append(phone_no)
        if email not in self.email:
            self.email.append (email)
    def update_name(self,old_name,new_name):
        if old_name in self.name:
            index=self.name.index(old_name)
            self.name[index]=new_name
    def update_phone(self,old_phone_no,new_phone_no):
        if old_phone_no in self.phone_no:
            index=self.phone_no.index(old_phone_no)
            self.phone_no[index]=new_phone_no
    def update_email(self,old_email,new_email):
        if old_email in self.email:
            index=self.phone_no.index(old_email)
            self.phone_no[index]=new_email
    def display(self):
        print("name",self.name,"\n")
        print("phone_no",self.phone_no,"\n")
        print("email",self.email,"\n")
        print("income tax details before update")
        a=income("sandhya",12345,"sandhya24@gmail.com")
        a.display()
print("income tax details after update")
income.update_name("sandhya","sandhyabws")
income.update_phone(12345,67854)
income.update_eamil("sandhya24@gmail.com","sandhyab1234@gmail.com")
income.display()