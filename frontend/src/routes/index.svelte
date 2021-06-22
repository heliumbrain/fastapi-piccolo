<script context="module">
	import { variables } from '$lib/variables';

	export const load = async ({ fetch }) => {
			const res = await fetch(`${variables.apiPath}/products`);
			const products = await res.json();
      console.log(products)
			return {
				props: {
					products
				}
			};
	};
</script>

<script>
	export let products = [];
</script>

<main>
	<div class="justify-center w-full">
		<h1 class="text-xl mx-auto text-center">FastAPI & Piccolo Example Project</h1>
		<p class="hover:caret-red-600 text-center">
			Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation
		</p>
		{#each products as product}
			<p>{product.name}</p>
		{/each}
	</div>
</main>
