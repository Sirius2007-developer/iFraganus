function randomId(){return Math.round(Math.random() * 999999)}

const themes = {
  light: {
    '--bg': '#deb887',
    '--color-text': '#000',
    '--del-btn': '#b10000',
    '--body-bg': '#f2f2f2',
    '--icon-color-light': '#fbf700',
    '--icon-color-dark': '#010101',
  },
  dark: {
    '--bg': '#111111',
    '--color-text': '#fff',
    '--del-btn': '#ffbb00',
    '--body-bg': '#232323',
    '--icon-color-light': '#fbf700',
    '--icon-color-dark': '#010101',
  },
  
}
// elements
const contentItems = document.querySelector('.content-items');
const taskForm = document.taskForm;
const titleinput = taskForm.elements.title;
const contentArea = taskForm.elements.content;
const btnTheme = document.querySelector('.navbar-btn')

// events
taskForm.addEventListener('submit', onFormSumbit)
btnTheme.addEventListener('click', selectTheme)
// document.addEventListener('DOMContentLoaded', loadCards)


function onFormSumbit(event){
  event.preventDefault()
  const ValueInp = titleinput.value
  const ValueArea = contentArea.value
  if (!ValueArea || !ValueInp) {
    alert('toliq malumotlarni kiriting')
    return
  }
}
function selectTheme(){
  let localThemeNeme
  if(btnTheme.classList.contains('light')){
    btnTheme.classList.remove('light')
    btnTheme.classList.add('dark')
    btnTheme.setAttribute('data-theme', 'dark')
  }else{
    btnTheme.classList.remove('dark')
    btnTheme.classList.add('light')
    btnTheme.setAttribute('data-theme','light')
  }
  const themeattr = btnTheme.getAttribute('data-theme');
  if(localStorage.getItem('theme') == null){
    localThemeNeme = themeattr
  }else{
    localThemeNeme = localStorage.getItem('theme')
  }
  localThemeNeme = themeattr
  const themeObj = themes[themeattr]
  let themestr =''
  for (const key in themeObj) {
    themestr += `${key}: ${themeObj[key]};`
    
  }
  localStorage.setItem('theme',(localThemeNeme))                                                                                                                                                                                                                                                                                                
  document.documentElement.style = themestr;
}
