package local.korkmatik.SanPlan;

import local.korkmatik.SanPlan.initialization.RoleInitializer;
import local.korkmatik.SanPlan.initialization.UserInitializer;
import local.korkmatik.SanPlan.models.user.Role;
import local.korkmatik.SanPlan.models.user.User;
import local.korkmatik.SanPlan.repositories.user.RoleRepository;
import local.korkmatik.SanPlan.repositories.user.UserRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.util.List;
import java.util.Set;

@SpringBootApplication
public class SanPlanApplication {

	public static void main(String[] args) {
		SpringApplication.run(SanPlanApplication.class, args);
	}

	@Bean
	CommandLineRunner init(RoleInitializer roleInitializer, UserInitializer userInitializer) {
		return args -> {
			Role adminRole = roleInitializer.createAdminRoleIfNotExists();
			roleInitializer.createUserRoleIfNotExists();

			userInitializer.createDummyAdminUser(adminRole);
		};
	}


}
