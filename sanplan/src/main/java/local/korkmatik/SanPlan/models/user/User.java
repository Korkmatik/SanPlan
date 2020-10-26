package local.korkmatik.SanPlan.models.user;

import lombok.*;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document
@NoArgsConstructor
@Data
public class User {

    @Id
    private int id;

    private String firstName;
    private String lastName;

    private String email;

    private ExecutiveQualification executiveQualification;
    private MedicalQualification medicalQualification;
}
