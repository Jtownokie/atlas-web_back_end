// Combining Filter and Map

export default function updateStudentGradeByCity(studentList, city, newGrades) {
  const studentsByLocation = studentList.filter((item) => item.location === city);

  return studentsByLocation.map((studentObj) => {
    const foundGrade = newGrades.find((gradeObject) => gradeObject.studentId === studentObj.id);

    if (foundGrade) {
      return { ...studentObj, grade: foundGrade.grade };
    } else {
      return { ...studentObj, grade: 'N/A' };
    }
  })
}
