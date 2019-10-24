--List the following details of each employee: employee number, last name, first name, gender, and salary.

--select * from employees;


Select e.emp_no,e.last_name,e.first_name,e.gender, s.salary from employees as e 
left join salaries as s on e.emp_no = s.emp_no
order by e.last_name;

--List employees who were hired in 1986
Select emp_no,last_name,first_name, gender,hire_date from employees WHERE EXTRACT (YEAR from hire_date)  = 1986
ORDER BY Last_name ASC;

--3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates
select e.emp_no, e.last_name,dm.dept_no,d.dept_name,dm.from_date,dm_to_date 
from employees as e join dept_manager as dm on e.emp_no = dm.emp_no
join departments dm on dm.dept_no = d.dept_no
order by e.last_name ASC;

-- List the department of each employee with the following information: employee number, last name, first name, and department name.
select e.emp_no, e.last_name,d.dept_name 
from employees as e join dept_emp as de on e.emp_no = de.emp_no
join departments d on de.dept_no = d.dept_no
--where (extract year from de.to_date) = 999
group by d.dept_name
order by e.last_name ASC;

--List all employees whose first name is "Hercules" and last names begin with "B."
select emp_no,first_name, last_name, gender from employees where first_name = 'Hercules'
and last_name like 'B%' 
order by last_name ASC;


--List all employees in the Sales department, including their employee number, last name, first name, and department name.
select e.emp_no, e.last_name,d.dept_name ,d.to_date
from employees as e join dept_emp as de on e.emp_no = de.emp_no
join departments d on de.dept_no = de.dept_no
where d.dept_name = "Sales"
order by e.last_name ASC;

--List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
select e.emp_no, e.last_name,d.dept_name ,d.to_date
from employees as e join dept_emp as de on e.emp_no = de.emp_no
join departments d on de.dept_no = de.dept_no
where d.dept_name in ('Sales','Development')
group by de.dept_name 
order by e.last_name ASC;

--in descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
select last_name,count (emp_no) as count_last_name from employees
group by last_name
order by count_last_name DESC;


