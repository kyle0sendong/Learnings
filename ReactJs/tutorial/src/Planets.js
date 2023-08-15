export const GasPlanet = (props) => {
    
    return (
        <div>
            {props.planets.map(
                (planet) => {
                    return planet.isGasPlanet && <p>{planet.name}</p>
                }
            )}
        </div>
    );
}