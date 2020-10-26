package local.korkmatik.SanPlan.models.user;

import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document
@Data
@NoArgsConstructor
public class Role {

    @Id
    private int id;

    private String name;
}
