package local.korkmatik.SanPlan;

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
	CommandLineRunner init(RoleRepository roleRepository, UserRepository userRepository, PasswordEncoder passwordEncoder) {
		return args -> {
			Role adminRole = createRoleIfNotExists(roleRepository, "ADMIN");
			createRoleIfNotExists(roleRepository, "USER");

			List<User> adminUsers = userRepository.findByRolesContains(adminRole);
			System.out.println(adminUsers);
			if (adminUsers.isEmpty()) {
				User adminUser = new User();
				adminUser.setFirstName("Admin");
				adminUser.setLastName("Admin");
				adminUser.setRoles(Set.of(adminRole));
				adminUser.setEmail("admin@localhost");
				adminUser.setEnabled(true);
				adminUser.setPassword(passwordEncoder.encode("admin"));
				userRepository.save(adminUser);
			}
		};
	}

	private Role createRoleIfNotExists(RoleRepository roleRepository, String admin) {
		Role role = roleRepository.findByRole(admin);
		if (role == null) {
			Role newRole = new Role();
			newRole.setRole(admin);
			roleRepository.save(newRole);
		}

		return role;
	}
}
