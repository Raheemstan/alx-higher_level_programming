#include <Python.h>
#include <stdio.h>

/* Function to print information about a Python list */
void print_python_list(PyObject *p)
{
    /* Check if the object is a valid Python list */
    if (!PyList_Check(p))
    {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    /* Get the size of the list */
    Py_ssize_t size = PyList_Size(p);

    /* Print list information */
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    /* Iterate through list elements and print their types */
    for (Py_ssize_t i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

/* Function to print information about Python bytes */
void print_python_bytes(PyObject *p)
{
    /* Check if the object is a valid Python bytes object */
    if (!PyBytes_Check(p))
    {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    /* Get the size of the bytes object */
    Py_ssize_t size = PyBytes_Size(p);

    /* Print bytes object information */
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);

    /* Get the string representation of the bytes object */
    const char *str = PyBytes_AsString(p);
    printf("  trying string: %s\n", str);

    /* Print the first 10 bytes of the object */
    printf("  first 10 bytes: ");
    for (Py_ssize_t i = 0; i < 10 && i < size; i++)
    {
        printf("%02x ", (unsigned char)str[i]);
    }
    printf("\n");
}

/* Function to print information about Python float */
void print_python_float(PyObject *p)
{
    /* Check if the object is a valid Python float object */
    if (!PyFloat_Check(p))
    {
        printf("[ERROR] Invalid Float Object\n");
        return;
    }

    /* Get the float value */
    double value = PyFloat_AsDouble(p);

    /* Print float object information */
    printf("[.] float object info\n");
    printf("  value: %lf\n", value);
}
