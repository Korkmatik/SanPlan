package local.korkmatik.SanPlan.models.user;

import lombok.*;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.index.IndexDirection;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.DBRef;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.Set;

@Document
@NoArgsConstructor
@AllArgsConstructor
@Data
public class User {

    @Id
    private int id;

    private String firstName;
    private String lastName;

    @Indexed(unique = true, direction = IndexDirection.DESCENDING)
    private String email;
    private boolean enabled;
    @DBRef
    private Set<Role> roles;
    private String password;

    private ExecutiveQualification executiveQualification;
    private MedicalQualification medicalQualification;
}
