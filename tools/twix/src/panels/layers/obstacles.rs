use std::str::FromStr;

use anyhow::Result;
use communication::CyclerOutput;
use eframe::epaint::{Color32, Stroke};
use nalgebra::Isometry2;
use types::Obstacle;

use crate::{panels::Layer, value_buffer::ValueBuffer};

pub struct Obstacles {
    robot_to_field: ValueBuffer,
    obstacles: ValueBuffer,
}

impl Layer for Obstacles {
    const NAME: &'static str = "Obstacles";

    fn new(nao: std::sync::Arc<crate::nao::Nao>) -> Self {
        let robot_to_field =
            nao.subscribe_output(CyclerOutput::from_str("control.main.robot_to_field").unwrap());
        let obstacles =
            nao.subscribe_output(CyclerOutput::from_str("control.main.obstacles").unwrap());
        Self {
            robot_to_field,
            obstacles,
        }
    }

    fn paint(
        &self,
        painter: &crate::twix_paint::TwixPainter,
        _field_dimensions: &types::FieldDimensions,
    ) -> Result<()> {
        let robot_to_field: Isometry2<f32> = self.robot_to_field.require_latest()?;
        let obstacles: Vec<Obstacle> = self.obstacles.require_latest()?;

        let hip_height_stroke = Stroke {
            width: 0.025,
            color: Color32::RED,
        };
        let foot_height_stroke = Stroke {
            width: 0.025,
            color: Color32::BLUE,
        };
        for obstacle in obstacles {
            painter.circle_stroke(
                robot_to_field * obstacle.position,
                obstacle.radius_at_hip_height,
                hip_height_stroke,
            );
            painter.circle_stroke(
                robot_to_field * obstacle.position,
                obstacle.radius_at_foot_height,
                foot_height_stroke,
            );
        }
        Ok(())
    }
}
