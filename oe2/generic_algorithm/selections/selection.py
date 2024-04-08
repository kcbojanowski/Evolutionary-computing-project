class SelectionMethod:

    def select(self, population, num_select):
        """
        Selects chromosomes from populaction

        Args:
        - population: list of chromosomes
        - num_select: Number of chromosomes to select

        Returns:
        - List of selected chromosomes
        """
        raise NotImplementedError("Implement select() method in subclass")