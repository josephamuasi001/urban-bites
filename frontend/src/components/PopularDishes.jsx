import FoodCard from "./FoodCard";

const foods = [

{
id:1,
name:"Spicy Chicken Wings",
restaurant:"Burger Hub",
rating:4.8,
price:52,
image:"https://images.unsplash.com/photo-1562967914-608f82629710?w=700"
},

{
id:2,
name:"Margherita Pizza",
restaurant:"Pizza Palace",
rating:4.7,
price:75,
image:"https://images.unsplash.com/photo-1513104890138-7c749659a591?w=700"
},

{
id:3,
name:"Creamy Alfredo",
restaurant:"Italian House",
rating:4.9,
price:68,
image:"https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=700"
},

{
id:4,
name:"Classic Burger",
restaurant:"Burger Hub",
rating:4.6,
price:48,
image:"https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=700"
}

];

function PopularDishes(){

return(

<section className="section">

<div className="section-header">

<div>

<span className="section-label">
FAVOURITES
</span>

<h2>Popular Dishes</h2>

<p>
Most loved meals from our restaurants.
</p>

</div>

<button className="btn btn-outline">
View All
</button>

</div>

<div className="food-grid">

{
foods.map(food=>(
<FoodCard
key={food.id}
food={food}
/>
))
}

</div>

</section>

);

}

export default PopularDishes;