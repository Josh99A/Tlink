// add hovered class to selected list item
let list = document.querySelectorAll(".navigation li");

function activeLink() {
  list.forEach((item) => {
    item.classList.remove("hovered");
  });
  this.classList.add("hovered");
}

list.forEach((item) => item.addEventListener("mouseover", activeLink));

// Menu Toggle
let toggle = document.querySelector(".toggle");
let navigation = document.querySelector(".navigation");
let main = document.querySelector(".main");

toggle.onclick = function () {
    main.classList.toggle("active");
    navigation.classList.toggle("active");
};



// PROFILE DROPDOWN
const profile = document.querySelector('.topbar .profile');
const imgProfile = profile.querySelector('.user-profile-img');
const dropdownProfile = profile.querySelector('.profile-links');

imgProfile.addEventListener('click', function () {
	dropdownProfile.classList.toggle('show');
})

