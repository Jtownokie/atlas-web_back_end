// Combining Filter and Map

export default function updateStudentGradeByCity(studentList, city, newGrades) {
  const studentsByLocation = studentList.filter((item) => item.location === city);

  return studentsByLocation.map((studentObj) => {
    const foundGrade = newGrades.filter((gradeObject) => gradeObject.studentId === studentObj.id);

    if (foundGrade[0]) {
      studentObj.grade = foundGrade[0].grade;
    } else {
      studentObj.grade = 'N/A';
    }
  })
}
