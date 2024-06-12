-- Computes average score by student id

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN proc_user_id INT
)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = proc_user_id;

    UPDATE users
    SET average_score = avg_score
    WHERE id = proc_user_id;
END $$

DELIMITER ;
