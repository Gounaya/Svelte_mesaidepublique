<script>
	export let name;
	import Card from "./Card.svelte";
	import GridCards from "./Grid_cards.svelte";

</script>


<style>
	
	main {
		background-color: #4696d7;
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: whitesmoke;
		font-size: 2em;
		font-weight: 500;
		margin-bottom: 80px;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>

<main>
	<h1>Récupérez les aides qui correspondent</h1>
	<GridCards/>
</main>