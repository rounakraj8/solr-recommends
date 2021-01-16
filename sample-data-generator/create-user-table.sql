CREATE TABLE `job_listing` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) DEFAULT NULL,
  `description` text,
  `organization_name` varchar(45) DEFAULT NULL,
  `organization_url` varchar(150) DEFAULT NULL,
  `locations` varchar(150) DEFAULT NULL,
  `primary_skills` varchar(150) DEFAULT NULL,
  `secondary_skills` varchar(150) DEFAULT NULL,
  `industry` varchar(150) DEFAULT NULL,
  `employment_type` enum('FULL TIME','PART TIME') DEFAULT NULL,
  `min_salary` decimal(10,0) DEFAULT '0',
  `max_salary` decimal(10,0) DEFAULT '100000000',
  `min_exp_yrs` decimal(10,0) DEFAULT '0',
  `max_exp_yrs` decimal(10,0) DEFAULT '99',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1;


