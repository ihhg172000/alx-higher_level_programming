#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: a PyObject struct that represents a Python object in C code.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;

	size = PyList_Size(p);
	allocated = ((PyListObject *) p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		PyTypeObject *type = Py_TYPE(item);

		printf("Element %ld: %s\n", i, type->tp_name);
	}
}

