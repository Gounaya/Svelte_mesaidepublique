<script>

import { onMount } from "svelte";
import Card from "./Card.svelte";



const addData = async function() {
    const url = 'https://dev.api.mesaidespubliques.fr/Aides/all?page=1&count=50'; 
    let cards_list = [];

    const response = await fetch(url, {mode: 'cors'}, { headers: { accept: "Accept: application/json" } })
        .catch(function(err) {
            console.log('Fetch Error :-S', err);
        });

    let data = await response.json();
    console.log("in ==> "+data.aides.length)
    for (let i = 0; i < data.aides.length; i++) {
        let item_data = {
            nature: data.aides[i].nature.title,
            title: data.aides[i].title,
            picture: data.aides[i].picture,
            description: data.aides[i].description,
        }
        cards_list.push(item_data)
    }
 
    result = cards_list;
}

const store = async () => {
    const all_data = 
    fetch(url, {mode: 'cors'}, { headers: { accept: "Accept: application/json" } })
    .then(async (response) => {
        response.json().then((response) => {
            let data_size = response.aides.length;

            for (let i = 0; i < data_size; i++) {

                let item_data = {
                    nature: response.aides[i].nature.title,
                    title: response.aides[i].title,
                    picture: response.aides[i].picture,
                    description: response.aides[i].description,
                }
                cards_list.push(item_data)
            }
            return cards_list;
        });
    })
    .catch(function(err) {
        console.log('Fetch Error :-S', err);
    });
    console.log(all_data)
};

let result = [];
addData();

</script>

<style>


    .content-grid {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        align-content: flex-start;
        position: relative;
        list-style-type: none;

    }
    
</style>



<div>
    <div class="content-grid-wrapper">
        <ul class="content-grid">
            {#each result as card_item}
                <Card {...card_item}/>
            {:else}
                <!-- this block renders when users.length === 0 -->
                <p> {result.length} loading...</p>
            {/each}
        </ul>
    </div>
</div>
