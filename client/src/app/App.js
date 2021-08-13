import SearchBar from '../components/SearchBar/SearchBar';
import style from './App.module.css';

function App() {
  return (
    <div className={style.app}>
      {/* Renderiza el componete search bar */}
      <SearchBar />
    </div>
  );
}

export default App;
