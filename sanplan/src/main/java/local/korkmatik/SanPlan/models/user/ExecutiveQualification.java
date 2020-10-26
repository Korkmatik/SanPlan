package local.korkmatik.SanPlan.models.user;

import lombok.*;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document
@NoArgsConstructor
@Data
public class ExecutiveQualification {

    @Id
    private int id;

    private String type;
    private String shortName;
}
