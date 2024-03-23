import os
import dao.daoConnection as dao
import models.clases as c
os.system('cls')
conex = dao.Connection("localhost", "root", "", "bdregisters")
conex.connect()

#instanciar modelo
city1 = c.City("Managua", 1)
city2 = c.City("León", 1)
city3 = c.City("Granada", 1)
city4 = c.City("Masaya", 1)
city5 = c.City("Estelí", 1)
city6 = c.City("Jinotepe", 1)

#instanciar dao
daoCity = dao.DaoCity(conex)
#insertar
daoCity.insert(city1)
daoCity.insert(city2)
daoCity.insert(city3)
daoCity.insert(city4)
daoCity.insert(city5)
daoCity.insert(city6)

cities = daoCity.get_all()
for city in cities:
    print(city)

#Instaciar modelo
Job1 = c.Job("Contador",1)
Job2 = c.Job("Secretaria",2)
Job3 = c.Job("R humanos",3)
Job4 = c.Job("Diseñador grafico",4)
Job5 = c.Job("Asesor de ventas",5)
Job6 = c.Job("Marketing digital",6)

#Instaciar dao
daoJob = dao.DaoJob(conex)
#Insertar
daoJob.insert(Job1)
daoJob.insert(Job2)
daoJob.insert(Job3)
daoJob.insert(Job4)
daoJob.insert(Job5)
daoJob.insert(Job6)

Jobs = daoJob.get_all()
for jobsj in Jobs:
    print(jobsj)

#instanciar modelo
Employee1 = c.Employee("Nahomy Bonilla",19,2,"30000",1)
Employee2 = c.Employee("Angela Alvarado",38,22,"16000",1)
Employee3 = c.Employee("Yadira Alvarado",33,8,"1000",1)
Employee4 = c.Employee("Angelly Bonilla",13,21,"2000",1)
Employee5 = c.Employee("Jose Lopez",46,25,"6000",1)
Employee6 = c.Employee("Enrique Gutierrez",26,19,"4000",1)
#Instanciar dao
daoEmployee = dao.DaoEmployee(conex)
#Insertar
daoEmployee.insert(Employee1)
daoEmployee.insert(Employee2)
daoEmployee.insert(Employee3)
daoEmployee.insert(Employee4)
daoEmployee.insert(Employee5)
daoEmployee.insert(Employee6)
#consultar

Employees = daoEmployee.get_all()
for employees in Employees:
    print(employees)
