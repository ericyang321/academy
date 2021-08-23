package perimeter

import "testing"

func TestArea(t *testing.T) {
	assertShape := func(tb testing.TB, shape Shape, expected float64) {
		tb.Helper()
		received := shape.Area()

		if expected != received {
			tb.Errorf("expected %f, but got %f", expected, received)
		}
	}
	t.Run("rectangles", func(t *testing.T) {
		rect := Rectangle{Width: 20.0, Height: 20.0}

		assertShape(t, rect, 400.0)
	})

	t.Run("circles", func(t *testing.T) {
		circle := Circle{Radius: 10.0}

		assertShape(t, circle, 314.1592653589793)
	})
}
