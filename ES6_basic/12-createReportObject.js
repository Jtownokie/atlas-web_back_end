// Report creation script

export default function createReportObject(employeesList) {
  const newObject = {
    allEmployees: {
      ...employeesList,
    },
    getNumberOfDepartments(employeesList) {
      const numDepartments = Object.keys(employeesList).length;

      return numDepartments;
    }
  }

  return newObject;
}
