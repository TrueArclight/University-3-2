package app.spring.deadsxnpai.repository;

import app.spring.deadsxnpai.entity.ClassEntity;
import org.springframework.data.repository.CrudRepository;

public interface ClassRepository extends CrudRepository<ClassEntity, Long> {
    ClassEntity findByCode(String code);
}
