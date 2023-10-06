#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, i;
    PyListObject *list;

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);

    list = (PyListObject *)p;
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}
