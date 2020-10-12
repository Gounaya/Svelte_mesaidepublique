<script>

    //export let nature;
    //export let picture;
    //export let title;
    //export let description;

</script>

<style>
    @import url(https://fonts.googleapis.com/css?family=Open+Sans);
    @import url(https://fonts.googleapis.com/css?family=Lato);
    
    body {
      background: #e3e3e3;
      font-family: 'Open Sans', 'Lato', sans-serif;
    }

 

    li:hover {
      background: rgba(228, 216, 54, .3);
    }
       
    img {
        width: 100px;
        height: 80px;
        margin: 0px auto 10px auto;

    }
    h2, h3 {
        text-overflow: ellipsis;
        white-space: nowrap;
        max-width: 280px;
        height: 22px;
    }
    h2 {
        font-size: 25px;
        font-weight: 600;
        margin-bottom: 4px;
    }

    .nature{
        color: gray;
        text-align: center;
        margin: auto;
        font-size: 15px;
		font-weight: 400;

    }

    .title{
        text-align: center;
        margin: auto auto 20px auto;
        white-space: pre-line;
        color: #FC9F5B;
        font-size: 10px;
    }

    p {
        font-size: 12px;
        color: rgb(71, 71, 71);
        width: 240px;
        white-space: initial;
    }
    .description{
       

    }
   
    .card{
        background-color: #fff;
        width: 240px;
        height: 400px;
        border: 2px solid #FC9F5B;
        border-radius: 2%;
        padding: 10px 10px;
        display: flex;
        flex-direction: column;
        justify-items: flex-start;
        align-items: flex-start;
        margin: 10px 10px;
        box-shadow: 5px 5px 20px 0px rgba(0,0,0,0.2);

    }

    button{
        padding: 15px 40px;
        background: rgb(60, 138, 255);
        color: #fff;
        border-radius: 30px;
        font-family: 'Open Sans', 'Lato', sans-serif;        
        font-size: 12px;
        position: relative;
        transition:         all .4s cubic-bezier(0.645, 0.045, 0.355, 1);
        cursor: pointer;
        display: block;
        margin: 30px auto 0px auto;
    }

    button::after,
    button::before{
        content: "";
        position: absolute;
        top: 50%;
        right: 0px;
        transform: translateY(-50%);
        opacity: 0;
        transition:         all .4s cubic-bezier(0.645, 0.045, 0.355, 1);
    }

    button::after{
        width: 30px;
        height: 1px;
        background: white;
        transform: translateX(-3px);
        margin-top: 0px;
    }

    button::before{
        content: "";
        transform: rotate(-135deg) translateX(50%);
        width: 11px;
        height: 11px;
        background: transparent;
        border-left: 1px solid white;
        border-bottom: 1px solid white;
    margin-top: -1px;
    }


    button:hover{
    padding: 15px 60px 15px 20px;
    }

    button:hover::after,
    button:hover::before{
        opacity: 1;
        right: 15px;
    }

    .savoir{
        text-decoration: none;
        color: rgb(60, 138, 255);
    }
    
</style>

<div class="card">
    <h2 class="nature">{$$props.nature}</h2>
    <img src={$$props.picture} alt="aslk"/>
    <h2 class="title">{$$props.title}</h2>
    <p class="description">the catchy phrase from Michaela ngelo Mich aelan geloM ichaela  ngeloMic hael angeloMi chaelan gelo Michael angelo</p>
    
    <button >
        Vérifier éligibilité
    </button>
    <p class="savoir"><a href="/">En Savoir plus</a></p>
</div>

