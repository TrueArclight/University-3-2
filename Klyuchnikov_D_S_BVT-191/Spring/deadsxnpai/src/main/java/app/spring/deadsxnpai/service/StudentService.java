package app.spring.deadsxnpai.service;

import app.spring.deadsxnpai.entity.ClassEntity;
import app.spring.deadsxnpai.entity.StudentEntity;
import app.spring.deadsxnpai.exceptions.StudentNotFoundException;
import app.spring.deadsxnpai.model.StudentModel;
import app.spring.deadsxnpai.repository.ClassRepository;
import app.spring.deadsxnpai.repository.StudentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class StudentService {
    @Autowired
    private StudentRepository studentRepository;
    @Autowired
    private ClassRepository classRepository;

    public StudentEntity createStudent(StudentEntity student, Long classId){
        ClassEntity classEntity = classRepository.findById(classId).get();
        student.setStudent(classEntity);
        return studentRepository.save(student);
    }
    public StudentModel getOne(long id) throws StudentNotFoundException {
        StudentEntity student = studentRepository.findById(id).get() ;
        if(student == null){
            throw new StudentNotFoundException("Ученик не найден");
        }
        return StudentModel.toModel(student);
    }

    public long deleteStudent(long id){
        studentRepository.deleteById(id);
        return id;
    }

}
